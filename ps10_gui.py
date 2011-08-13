import ps10; reload(ps10)
import wx, Queue
from wx.lib.newevent import NewEvent
from ps10 import *
from threading import Thread

WordSubmission, EVT_WORD_SUBMISSION = NewEvent()

class ModeFrame(wx.Frame):
    """
    This class is the main game mode selection menu.  It is the first window
    displayed, and is also re-displayed after each game.
    """
    def __init__(self):
        """
        Build up the GUI.
        """
        wx.Frame.__init__(self, parent = None, title = '6.00 Word Game',
                          size = (400, 80),
                          style = wx.DEFAULT_FRAME_STYLE &
                                  ~(wx.RESIZE_BORDER |
                                    wx.MAXIMIZE_BOX |
                                    wx.MINIMIZE_BOX))
        # Create the three buttons side by side; each one starts a different
        # game mode.
        mainPanel = wx.Panel(self, style = wx.TAB_TRAVERSAL)
        options = [('&Solo Game',    self.OnSolo),
                   ('Vs. &Computer', self.OnVsComp),
                   ('Vs. &Human',    self.OnVsHuman)]
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        for label, handler in options:
            button = wx.Button(mainPanel, label = label)
            button.Bind(wx.EVT_BUTTON, handler)
            hbox.Add(button, 1, wx.EXPAND | wx.ALL, border = 10)
        mainPanel.SetSizer(hbox)
        self.Center()
    def OnSolo(self, event):
        """
        Start a solo game.
        """
        self.Close()
        PlayFrame(HUMAN_SOLO).Show()
    def OnVsComp(self, event):
        """
        Start a vs. computer game.
        """
        self.Close()
        PlayFrame(HUMAN_VS_COMP).Show()
    def OnVsHuman(self, event):
        """
        Start a vs. human game.
        """
        self.Close()
        PlayFrame(HUMAN_VS_HUMAN).Show()

class PlayFrame(wx.Frame):
    """
    The main game-playing window.
    """
    def __init__(self, mode):
        """
        Build up the GUI.
        """
        wx.Frame.__init__(self, parent = None, title = '6.00 Word Game')
        self.mode = mode
        # There are four nested levels of panels.  The outerPanel contains the
        # status bar on the bottom and everything else on top of it (in
        # statsPanel).  statsPanel contains the stats display for player 1 on
        # the left, the mainPanel in the middle, and the stats display for
        # player 2 on the right.  mainPanel contains the history list box and
        # the entryPanel below it.  The entryPanel contains the inputBox and
        # the submitButton side by side.
        outerPanel = wx.Panel(self)
        statsPanel = wx.Panel(outerPanel)
        mainPanel = wx.Panel(statsPanel)
        entryPanel = wx.Panel(mainPanel)

        # entryPanel
        self.inputBox = wx.TextCtrl(entryPanel)
        self.submitButton = wx.Button(entryPanel, label = 'Enter!')
        self.submitButton.SetDefault()
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.inputBox, 1, wx.EXPAND)
        hbox.Add(self.submitButton, 0, wx.EXPAND)
        self.submitButton.Bind(wx.EVT_BUTTON, self.OnEnter)
        entryPanel.SetSizer(hbox)

        # mainPanel
        historyLabel = wx.StaticText(mainPanel,
                                     label = 'Previously entered words:')
        self.history = wx.ListBox(mainPanel)
        self.handLabel = wx.StaticText(mainPanel, label = 'Hand: ')
        inputBoxLabel = wx.StaticText(mainPanel, label =
                '&Enter word, or . to end round:')
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(historyLabel, 0, wx.EXPAND)
        vbox.Add(self.history, 1, wx.EXPAND)
        vbox.Add(self.handLabel, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 10)
        vbox.Add(inputBoxLabel, 0, wx.ALIGN_CENTER_VERTICAL)
        vbox.Add(entryPanel, 0, wx.EXPAND)
        mainPanel.SetSizer(vbox)

        # statsPanel
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        empty = lambda: wx.StaticText(statsPanel, label = '')
        self.stats = [
                wx.StaticText(statsPanel,
                              label = '',
                              style = wx.ALIGN_CENTER | wx.ST_NO_AUTORESIZE,
                              size = (150, -1))
                for player in [1,2] ]
        hbox.Add( self.stats[0], 0, wx.EXPAND )
        hbox.Add( mainPanel, 1, wx.EXPAND )
        hbox.Add( self.stats[1], 0, wx.EXPAND )
        statsPanel.SetSizer(hbox)

        # outerPanel
        self.statusBar = wx.StatusBar(outerPanel)
        self.statusBar.SetStatusText('This is the status bar.')
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add( statsPanel, 1, wx.EXPAND )
        vbox.Add( self.statusBar, 0, wx.EXPAND )
        outerPanel.SetSizer(vbox)

        # Set some miscellaneous options on the window.
        self.SetMinSize((700, 300))
        self.Center()

        # Bind some event handlers.
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(EVT_WORD_SUBMISSION, self.OnWordSubmission)

        # Start things up.
        self.queue = Queue.Queue()
        self.inputBox.SetFocus()
        self.StartGame()

    def OnClose(self, event):
        """
        Handle the event where the window is closed.
        """
        self.Destroy()
        frame = ModeFrame()
        frame.Show()
        frame.Raise()

    def OnEnter(self, event):
        """
        Handle the event where the submit button was pressed.
        """
        if self.submitButton.IsEnabled():
            self.TryWord(self.inputBox.GetValue())

    def OnWordSubmission(self, event):
        """
        Handle the event where the computer player has finished coming up with
        a word and tries to submit it.
        """
        self.queue.put(self.TryWord(event.word))

    def TryWord(self, word):
        """
        Common method called by OnEnter and OnWordSubmission.  This calls into
        the back-end to try this word, then the window displays are updated
        according to whether things succeeded or failed.

        returns: True if the game is still going, False if the game has ended.
        """
        try:
            try:
                # Call into the backend.
                points = self.game.tryWord(word)
                if points is not None:
                    # Succeeded, so add the word.
                    self.history.Insert(word, 0)
                    self.statusBar.SetStatusText('Got %d points.' % points)
                else:
                    # Failed, so just update the status bar.
                    self.statusBar.SetStatusText('Not a valid word.')
            finally:
                # In any case, clear the inputBox and refresh the stats
                # displays.
                self.inputBox.Clear()
                self.RefreshLabels()
            return True
        except EndHand:
            # We've reached the end of the hand, either voluntarily ('.') or by
            # using up all letters.

            # Summarize the hand.
            if word != '.' and word != '': self.history.Insert(word, 0)
            wx.MessageDialog(self,
                    message = "Player %d's hand ends." %
                        self.game.getCurrentPlayer().getIdNum(),
                    caption = 'End of hand',
                    style = wx.OK).ShowModal()
            if self.game.nextPlayer():
                # There is another player to switch to.
                self.StartHand()
            else:
                # Game has completely ended.
                if self.game.getNumPlayers() > 1:
                    if self.game.isTie():
                        wx.MessageDialog(self,
                                message = "Game ends in a tie.",
                                caption = "Game over",
                                style = wx.OK).ShowModal()
                    else:
                        wx.MessageDialog(self,
                                message = "Player %d wins!" % \
                                    self.game.getWinner().getIdNum(),
                                caption = "Game over",
                                style = wx.OK).ShowModal()
                self.Close()
            return False

    def RefreshLabels(self):
        """
        Refresh the displays in the stats labels and the hand label.
        """
        self.handLabel.SetLabel('Hand: %s' %
                self.game.getCurrentPlayer().getHand())
        for s, player in zip(self.stats, self.game.players):
            s.SetLabel(str(player))

    def StartGame(self):
        """
        Start a game by creating a wordlist and a game backend, then starting a
        hand.
        """
        wordlist = Wordlist()
        self.game = Game(self.mode, wordlist)
        self.StartHand()

    def StartHand(self):
        """
        Start a hand.
        """
        player = self.game.getCurrentPlayer()
        # Clear the history list box and refresh labels.
        self.history.Clear()
        self.RefreshLabels()
        # Prompt the user so that they can get ready.
        wx.MessageDialog(self,
                message = 'Press OK to begin!',
                caption = 'Starting new game',
                style = wx.OK).ShowModal()
        if type(player) == ComputerPlayer:
            # Disable controls.
            self.inputBox.Disable()
            self.submitButton.Disable()
            # The way for the worker thread to communicate to the reactor
            # thread is by posting events for the reactor to consume.  The
            # opposite direction is achieved using a synchronized queue.
            def submitWord(word):
                try:
                    wx.PostEvent(self, WordSubmission(word = word))
                    return self.queue.get()
                except:
                    return False
            # Start the computer player in a background thread.
            Thread(target = player.playHand,
                   args = (submitWord, self.game.wordlist)).start()
        else:
            # Enable controls.
            self.inputBox.Enable()
            self.submitButton.Enable()

if __name__ == '__main__':
    app = wx.App()
    frame = ModeFrame()
    frame.Show()
    app.MainLoop()

# vim:et:sw=4:ts=4

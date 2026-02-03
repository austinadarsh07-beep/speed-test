import wx
import random
import time

WORDS = [
    "apple","banana","cherry","date","elephant","forest","garden","house",
    "island","jungle","kite","lemon","mountain","notebook","orange","planet",
    "queen","river","sun","tree","umbrella","violin","window","xray","yacht",
    "zebra","cloud","rain","storm","wind","fire","water","earth","metal",
    "stone","light","dark","energy","power","speed","time","space","sound",
    "music","art","science","math","history","biology","physics","chemistry",
    "computer","python","keyboard","mouse","screen","internet","data","logic",
    "algorithm","function","variable","object","loop","array","string"
]

app = wx.App()
frame = wx.Frame(None, title="Typing Speed Test", size=(700, 400))
panel = wx.Panel(frame)

box = wx.BoxSizer(wx.VERTICAL)

target_words = random.sample(WORDS, 30)
target_text = " ".join(target_words)

display = wx.TextCtrl(panel, value=target_text,style=wx.TE_MULTILINE | wx.TE_READONLY)

input_box = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
result = wx.StaticText(panel, label="Start typing to begin...")

box.Add(display, 1, wx.EXPAND | wx.ALL, 10)
box.Add(input_box, 1, wx.EXPAND | wx.ALL, 10)
box.Add(result, 0, wx.ALIGN_CENTER | wx.ALL, 10)

panel.SetSizer(box)

start_time = None
finished = False

def on_char(event):
    global start_time
    if start_time is None and event.GetKeyCode() >= 32:
        start_time = time.time()
        result.SetLabel("Typing...")
    event.Skip()

def on_text(event):
    global finished
    text = input_box.GetValue()

    words_typed = text.strip().split()

    if len(words_typed) == 30 and text.endswith(" "):
        finished = True
        end_time = time.time()

        time_taken = end_time - start_time
        minutes = time_taken / 60

        correct = sum(1 for t, o in zip(words_typed, target_words) if t == o)

        wpm = int(correct / minutes)
        accuracy = (correct / 30) * 100

        result.SetLabel(
            f"WPM: {wpm} | Accuracy: {accuracy:.1f}% | Time: {time_taken:.0f}s"
        )

        input_box.SetEditable(False)

    event.Skip()

input_box.Bind(wx.EVT_CHAR, on_char)
input_box.Bind(wx.EVT_TEXT, on_text)

frame.Show()
app.MainLoop()

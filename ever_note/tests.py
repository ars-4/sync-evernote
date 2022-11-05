from evernote.api.client import EvernoteClient
from evernote.edam.type import ttypes


dev_token = "S=s1:U=96c96:E=18b9f419020:C=18447906420:P=1cd:A=en-devtoken:V=2:H=6dc76689bd3d682d7a503512381e3dfc"
client = EvernoteClient(token=dev_token)

userStore = client.get_user_store()
user = userStore.getUser()

note_store = client.get_note_store()

print(user)

notebooks = note_store.listNotebooks()

note = ttypes.Note()
note.title = "I'm a test note!"
notet = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
note.content = notet + '<en-note>Hello, world!</en-note>'
#note = note_store.createNote(note)

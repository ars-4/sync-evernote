from django.shortcuts import render
from django.http import HttpResponse
from evernote.edam.type import ttypes
from ever_note.info import client
from ever_note.forms import CreateNoteForm

# Create your views here.


def create_test_note(request):
    form = CreateNoteForm()
    note_store = client.get_note_store()
    if request.method == "POST":
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            note = ttypes.Note()
            note.title = data.get('title')
            notet = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
            note.content = notet + '<en-note>'+ data.get('description') +'</en-note>'
            note = note_store.createNote(note)
            return HttpResponse('Note Created Successfully: <a href="https://sandbox.evernote.com/shard/s1/sh/5931df73-db75-4678-9a41-6be2b83c33f2/73d78f4a3bf7c82e28b376f89ad11076">link</a>')
        else:
            return HttpResponse('Form is invalid')
    
    return render(request, 'ever_note/createNote.html', { 'form':form })

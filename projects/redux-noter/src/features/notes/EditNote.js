import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { noteEdited } from "./notesSlice";

function EditNote({ note }) {
  const [title, setTitle] = useState(note.title);
  const [content, setContent] = useState(note.content);
  const dispatch = useDispatch();

  const onTitleChanged = (e) => setTitle(e.target.value);
  const onContentChanged = (e) => setContent(e.target.value);

  const onSaveNoteClicked = () => {
    if (title && content) {
      dispatch(noteEdited(note.id, title, content));
      setTitle("");
      setContent("");
    }
  };

  return (
    <div>
      <input
        type="text"
        value={title}
        onChange={onTitleChanged}
        placeholder="Edit note title"
      />
      <textarea
        value={content}
        onChange={onContentChanged}
        placeholder="Edit note content"
      />
      <button onClick={onSaveNoteClicked}>Save Note</button>
    </div>
  );
}

export default EditNote;

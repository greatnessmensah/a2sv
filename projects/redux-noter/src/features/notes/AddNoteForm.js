import { useState } from "react";
import { noteAdded } from "./notesSlice";
import { useDispatch } from "react-redux";

import React from "react";

const AddNoteForm = () => {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const dispatch = useDispatch();

  const onTitleChanged = (e) => setTitle(e.target.value);
  const onContentChanged = (e) => setContent(e.target.value);

  const canSave = [title, content].every(Boolean);

  const onSavePostClicked = () => {
    if (canSave) {
      try {
        dispatch(noteAdded(title, content));

        setTitle("");
        setContent("");
      } catch (err) {
        console.error("Failed to save the post", err);
      }
    }
  };

  return (
    <section>
      <h2>Add a New Note</h2>
      <form>
        <label>Post Title:</label>
        <input
          type="text"
          value={title}
          onChange={onTitleChanged}
        />
        <textarea
          id="postContent"
          name="postContent"
          value={content}
          onChange={onContentChanged}
        />
        <button type="button" className="bg-black text-white rounded-md w-24" onClick={onSavePostClicked} disabled={!canSave}>
          Save Post
        </button>
      </form>
    </section>
  )
};

export default AddNoteForm;

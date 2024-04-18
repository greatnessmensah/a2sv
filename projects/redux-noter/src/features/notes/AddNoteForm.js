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
      <div className="flex flex-col justify-center mt-5">
        <div className="flex justify-center text-2xl">Redux Noter</div>
        <div className="flex justify-center">
          <form className="flex flex-col sm:w-11/12 lg:w-7/12">
            <input className="mb-2 rounded-sm h-2/4"
              type="text"
              value={title}
              onChange={onTitleChanged}
              placeholder="Note tile"
            />
            <textarea className="sm:w-full mb-2 rounded-sm h-5/6"
              placeholder="Add a new note"
              value={content}
              onChange={onContentChanged}
            />
            <button
              type="button"
              className="bg-black text-white rounded-md w-24"
              onClick={onSavePostClicked}
              disabled={!canSave}
            >
              Save Post
            </button>
          </form>
        </div>
      </div>
    </section>
  );
};

export default AddNoteForm;

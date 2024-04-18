import React, { useState } from "react";
import { RiDeleteBin4Line } from "react-icons/ri";
import { FaEdit } from "react-icons/fa";
import { useDispatch, useSelector } from "react-redux";
import { selectAllNotes, noteDeleted } from "./notesSlice";
import TimeAgo from "./TimeAgo";
import { noteEdited } from "./notesSlice";


const NotesList = () => {
  let notes = useSelector(selectAllNotes);
  const [isEditing, setIsEditing] = useState(false);
  notes = [...notes].sort((a, b) => new Date(b.date) - new Date(a.date));
  const dispatch = useDispatch();

  const onDeleteNoteClicked = (id) => {
    dispatch(noteDeleted(id));
  };

  const renderedNotes = notes.map((note) => {
  
    const onEditNoteClicked = () => {
      setIsEditing(!isEditing);
    };
  
    return (
      <article
        className="flex flex-col items-center relative bg-gray-200 rounded-lg mx-auto w-9/12 h-64 m-2"
        key={note.id}
      >
        {isEditing ? (
          <input
            type="text"
            className="m-2"
            defaultValue={note.title}
            onBlur={(e) => dispatch(noteEdited({ id: note.id, title: e.target.value }))}
          />
        ) : (
          <div className="text-2xl px-2 font-bold">{note.title}</div>
        )}
        {isEditing ? (
          <textarea
            defaultValue={note.content}
            onBlur={(e) => dispatch(noteEdited({ id: note.id, content: e.target.value }))}
          />
        ) : (
          <p className="text-left font-semibold text-lg ">{note.content}</p>
        )}
        <div className="absolute bottom-0 left-2 ">
          <button onClick={() => onDeleteNoteClicked(note.id)}>
            <RiDeleteBin4Line />
          </button>
          <button className="ml-3" onClick={onEditNoteClicked}>{isEditing ? 'Save' : <FaEdit />}
          </button>
        </div>
        <div className="absolute font-light italic bottom-0 right-2">
          <TimeAgo timestamp={note.date} />
        </div>
      </article>
    );
  });

  return (
    <section>
      <div className="flex justify-center">
        {/* <p className="flex self-center py-20 text-6xl">My Notes</p> */}
      </div>
      <div className="mx-auto sm:grid grid-1 lg:grid grid-cols-3 w-auto justify-items-stretch">
        {renderedNotes}
      </div>
    </section>
  );
};

export default NotesList;

import { createSlice, nanoid } from "@reduxjs/toolkit";
import { sub } from "date-fns";

const initialState = [
  {
    id: nanoid(),
    title: "my first note",
    content: "my first content",
    date: sub(new Date(), { minutes: 20 }).toISOString(),
  },
];

const notesSlice = createSlice({
  name: "notes",
  initialState,
  reducers: {
    noteAdded: {
      reducer(state, action) {
        state.push(action.payload);
      },
      prepare(title, content) {
        return {
          payload: {
            id: nanoid(),
            title,
            content,
            date: new Date().toISOString(),
          },
        };
      },
    },
    noteEdited: {
      reducer(state, action) {
        const { id, title, content } = action.payload;
        const existingNote = state.find((note) => note.id === id);
        if (existingNote) {
          existingNote.title = title;
          existingNote.content = content;
          existingNote.date = new Date().toISOString();
        }
      },
    },
    noteDeleted: {
      reducer(state, action) {
        const id = action.payload;
        const index = state.findIndex((note) => note.id === id);
        if (index !== -1) {
          state.splice(index, 1);
        }
      },
    },
  },
});

export const selectAllNotes = (state) => state.notes;

export const { noteAdded, noteEdited, noteDeleted } = notesSlice.actions;

export default notesSlice.reducer;

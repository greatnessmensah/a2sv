import { createSlice, nanoid } from "@reduxjs/toolkit";
import { sub } from "date-fns";

const initialState = [
  {
    id: nanoid(),
    title: "my first note",
    content: "my first content",
    date: sub(new Date(), { minutes: 20 }).toISOString(),
  },
  {
    id: nanoid(),
    title: "my second note",
    content: "my second content",
    date: sub(new Date(), { minutes: 10 }).toISOString(),
  },
  {
    id: nanoid(),
    title: "my third note",
    content: "my third content",
    date: sub(new Date(), { minutes: 30 }).toISOString(),
  },
  {
    id: nanoid(),
    title: "my fourth note",
    content: "my fourth content",
    date: sub(new Date(), { minutes: 30 }).toISOString(),
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
        }
      },
      prepare(id, title, content) {
        return {
          payload: {
            id,
            title,
            content,
            date: new Date().toISOString(),
          },
        };
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

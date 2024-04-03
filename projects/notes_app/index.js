const _ = require("lodash");
const { program } = require("commander");
const fs = require("fs");

function getNotes() {
  try {
    const data = fs.readFileSync("db.json");
    return JSON.parse(data);
  } catch (error) {
    return [];
  }
}

function saveNotes(notes) {
  fs.writeFileSync("db.json", JSON.stringify(notes, null, 2));
}

function addNote(title, content) {
  const database = getNotes();
  const lastNote = _.last(database);
  const newId = lastNote && lastNote.id ? lastNote.id + 1 : 1;
  const newNote = {
    id: newId,
    title: title,
    content: content,
    created_at: new Date(),
    updated_at: new Date(),
  };
  database.push(newNote);
  saveNotes(database);
}

function getNoteById(id) {
  const database = getNotes();
  const note = _.find(database, (note) => Number(note.id) === Number(id));
  if (!note) {
    return `Note with id: ${id} not found`;
  }
  return note;
}

function updateNoteById(id, title, content) {
  const database = getNotes();
  const note = _.find(database, (note) => Number(note.id) === Number(id));
  if (note) {
    note.title = title;
    note.content = content;
    note.updated_at = new Date();
    saveNotes(database);
  }
  return note;
}

function deleteNoteById(id) {
  const database = getNotes();
  const noteIndex = _.findIndex(
    database,
    (note) => Number(note.id) === Number(id)
  );
  if (noteIndex !== -1) {
    _.pullAt(database, noteIndex);
    saveNotes(database);
  }
  return `Note with id: ${id} deleted successfully`;
}

function searchNotes(query, chunkSize = 10) {
  const database = getNotes();
  const lowerCaseQuery = query.toLowerCase();
  const results = _.filter(
    database,
    (note) =>
      note.title.toLowerCase().includes(lowerCaseQuery) ||
      note.content.toLowerCase().includes(lowerCaseQuery)
  );
  return _.chunk(results, chunkSize);
}

function getLatestNotes() {
  const database = getNotes();
  return _.sortBy(database, (note) => -new Date(note.updated_at));
}

program.version("0.0.1").description("Notter: A Note Taking CLI App");

program
  .command("add <title> <content>")
  .alias("a")
  .description("Add a note")
  .action((title, content) => {
    const debouncedAddNote = _.debounce(addNote, 500);
    debouncedAddNote(title, content);
  });

program
  .command("getall")
  .alias("ga")
  .description("Get all notes")
  .action(() => {
    console.log(getNotes());
  });

program
  .command("get <id>")
  .alias("g")
  .description("Get a note by id")
  .action((id) => {
    console.log(getNoteById(id));
  });

program
  .command("update <id> <title> <cotent>")
  .alias("u")
  .description("Update a note by id")
  .action((id, title, content) => {
    updateNoteById(id, title, content);
  });

program
  .command("delete <id>")
  .alias("d")
  .description("Delete Note by id")
  .action((id) => {
    console.log(deleteNoteById(id));
  });

program
  .command("search <query>")
  .alias("s")
  .description("Search through notes by query")
  .action((query) => {
    console.log(searchNotes(query));
  });

program
  .command("getlatest")
  .alias("gl")
  .description("Get Latest Notes")
  .action(() => {
    console.log(getLatestNotes());
  });

program.parse(process.argv);

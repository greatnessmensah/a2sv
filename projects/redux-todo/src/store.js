import { configureStore } from '@reduxjs/toolkit'

import todosReducer from './features/todos/todosSlice'
import filtersReducer from './features/filters/filtersSlice'
// initializing the store
const store = configureStore({
  reducer: {
    todos: todosReducer,
    filters: filtersReducer,
  },
})

export default store
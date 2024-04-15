const dev = process.env.NODE_ENV !== 'production'

export const server = dev ? 'https://jsonplaceholder.typicode.com/posts' : 'https://jsonplaceholder.typicode.com/posts'
import React, { useState, useEffect } from "react";
import { useRouter } from 'next/router';
import styles from "../../../styles/Edit.module.css";

export default function PostForm() {
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  const router = useRouter();
  const { id } = router.query;

  useEffect(() => {
    if (id) {
      fetchPostDetails(id);
      document.title = `Editing Post: ${id}`
    }
  }, [id]);

  const fetchPostDetails = async (id) => {
    const response = await fetch(
      `https://jsonplaceholder.typicode.com/posts/${id}`
    );
    const post = await response.json();
    setTitle(post.title);
    setBody(post.body);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsSubmitting(true);
    let date = new Date().toUTCString();

    let data = await editPost(id, { title, body, date });

    setTitle("");
    setBody("");
    setIsSubmitting(false);
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit} className={styles.card}>
      <div>
        <label htmlFor="title">Title:</label>
        <input
          type="text"
          id="title"
          className={styles.input}
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
      </div>
      <div>
        <label htmlFor="body">Body:</label>
        <textarea
          className={styles.input}
          id="body"
          value={body}
          onChange={(e) => setBody(e.target.value)}
          required
        />
      </div>
      <button type="submit" className={styles.button} disabled={isSubmitting}>
        {isSubmitting
          ? "Submitting..."
          : "Edit Post"}
      </button>
    </form>
  );
}

async function editPost(id, article) {
  try {
    const response = await fetch(
      `https://jsonplaceholder.typicode.com/posts/${id}`,
      {
        method: "PATCH",
        body: JSON.stringify(article),
        headers: {
          "Content-Type": "application/json; charset=UTF-8",
        },
      }
    );

    if (!response.ok) {
      throw new Error("Failed to edit the post");
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error editing post:", error);
    return null;
  }
}

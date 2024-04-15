import ArticleList from "../components/ArticleList";
import Link from "next/link";
import styles from "../styles/Home.module.css"

export default function Home({ articles }) {
  return (
    <div>
      <Link href="/article/create" >
        <button className={styles.button}>Create Post</button>
      </Link>
      <ArticleList articles={articles} />
    </div>
  );
}

export const getStaticProps = async () => {
  const res = await fetch(`https://jsonplaceholder.typicode.com/posts`);
  const articles = await res.json();

  return {
    props: {
      articles,
    },
  };
};

import ArticleList from "../components/ArticleList";
import { server } from "../config";

export default function Home({ articles }) {
  return (
    <div>
      <ArticleList articles={articles} />
    </div>
  );
}

export const getStaticProps = async () => {
  const res = await fetch(
    `https://my-json-server.typicode.com/greatnessmensah/a2sv/articles`
  );
  const articles = await res.json();

  return {
    props: {
      articles,
    },
  };
};

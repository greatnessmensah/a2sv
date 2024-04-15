import React from "react";
import articleStyles from "../styles/Article.module.css";
import Link from "next/link";
import { BiEdit } from "react-icons/bi";
const ArticleItem = ({ article }) => {
  return (
    <div>
      <div className={articleStyles.card}>
        <Link href={`/article/${article.id}`}>
          <h3>{article.title} &rarr;</h3>
        </Link>
        <p>{article.excerpt}</p>
        <Link href={`/article/edit/${article.id}`}>
          <button className={articleStyles.button}>
          <BiEdit />
          </button>
        </Link>
      </div>
    </div>
  );
};

export default ArticleItem;

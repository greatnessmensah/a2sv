import React from "react";
import Avatar from "./Avatar";
import Info from "./Info";
import { UserProfile } from "../data";

interface CardProps {
  user: UserProfile;
}

const Card: React.FC<CardProps> = ({ user }) => {
  return (
    <div className="card">
      <Avatar imageUrl={user.imageUrl} name={user.name} />
      <Info name={user.name} bio={user.bio} website={user.website} />
    </div>
  );
};

export default Card;

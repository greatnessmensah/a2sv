import React from "react";
import Avatar from "./Avatar";
import Info from "./Info";
import { UserProfile } from "../data";

// Declared Props which takes a UserProfile object
interface CardProps {
  user: UserProfile;
}

const Card: React.FC<CardProps> = ({ user }) => {
  return (
    <div className="card">
      {/* Pass in the Avatar and Info components to be rendered on the cards */}
      <Avatar imageUrl={user.imageUrl} name={user.name} />
      <Info name={user.name} bio={user.bio} website={user.website} />
    </div>
  );
};

export default Card;

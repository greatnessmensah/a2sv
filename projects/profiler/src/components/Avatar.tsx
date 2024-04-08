import React from "react";

interface AvatarProps {
  imageUrl?: string;
  name: string;
}

const Avatar: React.FC<AvatarProps> = ({ imageUrl, name }) => {
  if (imageUrl) {
    return <img src={imageUrl} alt="Avatar" className="avatar" />;
  } else {
    const initials = name
      .split(" ")
      .map((word) => word[0])
      .join("");
    return <div className="avatar" style={{backgroundColor: '#2f54c3'}}>{initials}</div>;
  }
};

export default Avatar;

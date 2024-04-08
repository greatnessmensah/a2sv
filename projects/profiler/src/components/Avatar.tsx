import React from "react";

// Props takes the imgae url and name
interface AvatarProps {
  imageUrl?: string;
  name: string;
}

const Avatar: React.FC<AvatarProps> = ({ imageUrl, name }) => {
  // Conditionally renders image if it exists else it displays the initials of the name
  if (imageUrl) {
    return <img src={imageUrl} alt="Avatar" className="avatar" />;
  } else {
    const initials = name
      .split(" ")
      .map((word) => word[0])
      .join("");
      // only add background color if it is displaying initials
    return <div className="avatar" style={{backgroundColor: '#2f54c3'}}>{initials}</div>;
  }
};

export default Avatar;

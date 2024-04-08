import React from "react";

interface InfoProps {
  name: string;
  bio: string;
  website?: string;
}

const Info: React.FC<InfoProps> = ({ name, bio, website }) => {
  return (
    <div className="info">
      <h2>{name}</h2>
      <p>{bio}</p>
      {website && <button className="button"><a href={website}>Website</a></button>}
    </div>
  );
};

export default Info;

import React from "react";

// Declaring Props which works like a struct for the info you need to pass
interface InfoProps {
  name: string;
  bio: string;
  website?: string;
}
// Passed props into app 
const Info: React.FC<InfoProps> = ({ name, bio, website }) => {
  return (
    <div className="info">
      <h2>{name}</h2>
      <p>{bio}</p>
      {/* Used condtional rendereing to show website link if it exists */}
      {website && <button className="button"><a href={website}>Website</a></button>}
    </div>
  );
};

export default Info;

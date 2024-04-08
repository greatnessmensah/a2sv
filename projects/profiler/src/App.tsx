import React from "react";
import "./App.css";
import Card from "./components/Card";
import { userProfiles, UserProfile } from "./data";

const App: React.FC = () => {
  return (
    <div className="App">
      <div className="card-container">
        {/* Rendereing the userProfiles in data.js as a list using map, by default 
        react uses the indexes of the objects but it is better to an id  */}
        {userProfiles.map((user: UserProfile) => (
          <Card key={user.id} user={user} />
        ))}
      </div>
    </div>
  );
};

export default App;

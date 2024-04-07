import React from "react";
import "./App.css";
import Card from "./components/Card";
import { userProfiles, UserProfile } from "./data";

const App: React.FC = () => {
  return (
    <div className="App">
      <div className="card-container">
        {userProfiles.map((user: UserProfile) => (
          <Card key={user.id} user={user} />
        ))}
      </div>
    </div>
  );
};

export default App;

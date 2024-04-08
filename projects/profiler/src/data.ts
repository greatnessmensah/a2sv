const avatar1 = require("./images/avatar1.png")
const avatar2 = require("./images/avatar2.png")
const avatar3 = require("./images/avatar3.png")

export interface UserProfile {
  id: number;
  name: string;
  bio: string;
  deparment?: string;
  website?: string;
  imageUrl?: string;
}

export const userProfiles: UserProfile[] = [
  {
    id: 1,
    name: "John Doe",
    deparment: "Engineering",
    bio: "Software Engineer",
    website: "https://johndoe.com",
    imageUrl: avatar1,
  },
  {
    id: 2,
    name: "Jane Smith",
    deparment: "Research",
    bio: "Physicist",
    website: "https://janesmith.com",
    imageUrl: avatar2,
  },
  {
    id: 3,
    name: "Bob Johnson",
    deparment: "Marine Biology",
    bio: "Marine Scientist",
    imageUrl: avatar3,
  },
  {
    id: 4,
    name: "Hannah Mason",
    deparment: "Engineering",
    bio: "Electrical Engineer",
    website: "https://alicebrown.com",
  },
];

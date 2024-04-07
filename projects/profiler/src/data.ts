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
      name: 'John Doe',
      deparment: 'Engineering',
      bio: 'Software Engineer',
      website: 'https://johndoe.com',
      imageUrl: './public/avatar1.png',
    },
    {
      id: 2,
      name: 'Jane Smith',
      deparment: 'Research',
      bio: 'Physicist',
      website: 'https://janesmith.com',
      imageUrl: './public/avatar2.png',
    },
    {
      id: 3,
      name: 'Bob Johnson',
      deparment: 'Marine Biology',
      bio: 'Marine Scientist',
      imageUrl: './public/avatar3.png',
    },
    {
      id: 4,
      name: 'Alice Brown',
      deparment: 'Engineering',
      bio: 'Electrical Engineer',
      website: 'https://alicebrown.com',
    }
  ];
// profiles.ts

export interface UserProfile {
    id: number;
    name: string;
    bio: string;
    deparment?: string;
    website?: string;
  }
  
  export const userProfiles: UserProfile[] = [
    {
      id: 1,
      name: 'John Doe',
      deparment: 'Engineering',
      bio: 'Software Engineer',
      website: 'https://johndoe.com',
    },
    {
      id: 2,
      name: 'Jane Smith',
      deparment: 'Research',
      bio: 'Physicist',
      website: 'https://janesmith.com',
    },
    {
      id: 3,
      name: 'Bob Johnson',
      deparment: 'Marine Biology',
      bio: 'Marine Scientist',
    },
    {
      id: 4,
      name: 'Alice Brown',
      bio: 'Electrical Engineer',
      website: 'https://alicebrown.com',
    }
  ];
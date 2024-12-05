import { Character } from '../models/character.interface';

export const CHARACTERS: Character[] = [
  {
    id: '1',
    name: 'Deviluna',
    server: 'Abaton',
    company: 'Zoo Magique',
    role: 'Tank',
    gearScore: 650,
    primaryWeapon: 'Sword and Shield',
    secondaryWeapon: 'War Hammer',
    userId: '1', // corresponds to fu.dev1
    createdAt: new Date('2022-01-01'),
    updatedAt: new Date('2024-01-01'),
  },
  {
    id: '2',
    name: 'Devilune',
    server: 'Apu',
    company: 'Black Town',
    role: 'Healer',
    gearScore: 650,
    primaryWeapon: 'Sword and Shield',
    secondaryWeapon: 'War Hammer',
    userId: '1', // corresponds to fu.dev1
    createdAt: new Date('2022-01-01'),
    updatedAt: new Date('2024-01-01'),
  },
];
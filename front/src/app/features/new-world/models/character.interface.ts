export interface Character {
    id: string;
    name: string;
    server: string;
    company?: string;
    role: 'Tank' | 'Healer' | 'Support' | 'Bruiser' | 'Melee Dex' | 'Ranged Dex' | 'undefined';
    faction?: 'covenant' | 'marauder' | 'syndicate';
    primaryWeapon: string;
    secondaryWeapon: string;
    userId: string;
    createdAt: Date;
    updatedAt: Date;
    gearScore: number;
}

export const WEAPONS = [
    'Sword and Shield',
    'Great Axe',
    'War Hammer',
    'Spear',
    'Hatchet',
    'Rapier',
    'Bow',
    'Musket',
    'Fire Staff',
    'Life Staff',
    'Ice Gauntlet',
    'Void Gauntlet'
] as const;

export const ROLES = [
    'Tank',
    'Healer',
    'Support',
    'Bruiser',
    'Melee Dex',
    'Ranged Dex',
] as const;

export const SERVERS = [
    'Abaton',
    'Dry Tree',
    'Barri',
    'Nysa',
    'Tartarus',
] as const;

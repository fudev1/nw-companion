export interface Guild {
    id: string;
    name: string;
    region: string;
    server: string;
    ownerId: string;
    ownerCharacterId: string;
    createdAt: Date;
}

export type Region = 'EU Central' | 'US East' | 'US West' | 'SA East' | 'AP Southeast';

export const REGIONS: Region[] = [
    'EU Central',
    'US East',
    'US West',
    'SA East',
    'AP Southeast'
];

export const SERVERS: Record<Region, string[]> = {
    'EU Central': ['Abaton', 'Asgard', 'Barri', 'Hellheim'],
    'US East': ['Olympus', 'Valhalla', 'Yggdrasil'],
    'US West': ['Camelot', 'El Dorado'],
    'SA East': ['Devaloka', 'Irkalla'],
    'AP Southeast': ['Delos', 'Eridu']
  };
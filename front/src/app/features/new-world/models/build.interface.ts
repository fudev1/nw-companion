export type BuildType = 'PvE' | 'PvP';
export type BuildRole = 'Tank' | 'Healer' | 'DPS';
export type BuildStatus = 'active' | 'inactive';

export interface Build {
    id: string;
    name: string;
    type: BuildType;
    role: BuildRole;
    status: BuildStatus;
    primaryWeapon: string;
    secondaryWeapon: string;
    gearScore: number;
    description?: string;
    characterId: string;
    createdAt: string;
    updatedAt: string;
}
export interface Company {
    id: string;
    name: string;
    faction: 'covenant' | 'marauder' | 'syndicate';
    server: string;
    territories?: string[];
    memberCount: number
    governor: string;
    consul: string;
    createdAt: Date;
}
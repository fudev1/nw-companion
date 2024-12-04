import { Company } from '../models/companies.interface';

export const COMPANIES: Company[] = [
    {
        id: '1',
        name: 'Zoo Magique',
        faction: 'covenant',
        server: 'Abaton',
        territories: ['EverFall', 'Windsward'],
        memberCount: 99,
        governor: 'ImQS',
        consul: 'Migi',
        createdAt: new Date('2022-01-01')
    },
    {
        id: '2',
        name: 'Mascarade',
        faction: 'marauder',
        server: 'Abaton',
        territories: ['Monarchs Bluffs'],
        memberCount: 81,
        governor: 'Watha',
        consul: 'BattleMaster',
        createdAt: new Date('2022-01-01')
    },
    {
        id: '3',
        name: 'Black Town',
        faction: 'syndicate',
        server: 'Abaton',
        territories: [''],
        memberCount: 55,
        governor: 'A7',
        consul: 'XCloud',
        createdAt: new Date('2022-01-01')
    },
]
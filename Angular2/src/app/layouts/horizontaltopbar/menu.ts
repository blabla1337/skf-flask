import { MenuItem } from './menu.model';

export const MENU: MenuItem[] = [
    {
        id: 1,
        label: 'Dashboards',
        icon: 'mdi mdi-18px mdi-view-dashboard mr-2',
        link: '/dashboard',
    },
    {
        id: 2,
        label: 'Manage Projects',
        icon: 'mdi mdi-18px mdi-card-bulleted mr-2',
        link: '/projects/manage',
    },
    {
        id: 3,
        icon: 'mdi mdi-18px mdi-account-multiple mr-2',
        label: 'Users',
        link: 'users/manage'
    },
    {
        id: 4,
        icon: 'mdi mdi-18px mdi-text-box-check mr-2',
        label: 'Checklists',
        link: 'checklists/view',
    },
    {
        id: 5,
        label: 'Code examples',
        icon: 'mdi mdi-18px mdi-code-greater-than-or-equal mr-2',
        link: 'code-example/view'
    },
    {
        id: 6,
        label: 'Knowledgebase',
        icon: 'mdi mdi-18px mdi-code-greater-than-or-equal mr-2',
        link: 'knowledgebase/read'
    },
    {
        id: 7,
        label: 'Code examples',
        icon: 'mdi mdi-18px mdi-code-greater-than-or-equal mr-2',
        link: 'labs/view'
    },
];


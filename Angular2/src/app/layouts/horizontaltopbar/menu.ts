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
        icon: 'mdi mdi-18px mdi-code-greater-than-or-equal mr-2',
        label: 'Code Examples',
        link: '/code-example/view'
    },
    {
        id: 4,
        icon: 'mdi mdi-18px mdi-text-box-check mr-2',
        label: 'Checklists',
        link: '/checklists/view',
    },
    {
        id: 5,
        label: 'Knowledgebase',
        icon: 'mdi mdi-18px mdi-school mr-2',
        link: '/knowledgebase/read'
    },
    {
        id: 6,
        label: 'Users',
        icon: 'mdi mdi-18px mdi-account-edit mr-2',
        link: '/users/manage'
    },
    {
        id: 7,
        label: 'Labs',
        icon: 'mdi mdi-18px mdi-flask mr-2',
        link: '/labs/view'
    },
];

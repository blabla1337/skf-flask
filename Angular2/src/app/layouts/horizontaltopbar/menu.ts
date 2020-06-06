import { MenuItem } from './menu.model';

export const MENU: MenuItem[] = [
    {
        id: 1,
        label: 'Dashboards',
        icon: 'bx-home-circle',
    },
    {
        id: 2,
        label: 'Manage Projects',
        icon: 'bx-tone',
        isUiElement: true,
    },
    {
        id: 3,
        label: 'Users',
    },
    {
        id: 4,
        icon: 'bx-collection',
        label: 'Checklists',
    },
    {
        id: 5,
        label: 'Code examples',
        icon: 'bx-file',
    }
];


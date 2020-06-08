import { MenuItem } from './menu.model';
import { UseExistingWebDriver } from 'protractor/built/driverProviders';
import { userInfo } from 'os';

export const MENU: MenuItem[] = [
    {
        id: 1,
        label: 'Dashboards',
        icon: 'mdi mdi-18px mdi-view-dashboard mr-2',
    },
    {
        id: 2,
        label: 'Manage Projects',
        icon: 'mdi mdi-18px mdi-card-bulleted mr-2',
        isUiElement: true,
    },
    {
        id: 3,
        icon: 'mdi mdi-18px mdi-account-multiple mr-2',
        label: 'Users',
    },
    {
        id: 4,
        icon: 'mdi mdi-18px mdi-text-box-check mr-2',
        label: 'Checklists',
    },
    {
        id: 5,
        label: 'Code examples',
        icon: 'mdi mdi-18px mdi-code-greater-than-or-equal mr-2',
    }
];


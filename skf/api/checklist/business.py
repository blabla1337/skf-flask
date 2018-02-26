from skf.database import db
from skf.api.security import log, val_num, val_float
from skf.database.checklists import checklists
from skf.database.checklists_kb import checklists_kb


def get_checklist_item(checklist_id):
    log("User requested specific checklist item", "LOW", "PASS")
    val_float(checklist_id)
   
    result = checklists_kb.query.filter(checklists_kb.checklistID == checklist_id).one()
    return result


def get_checklist_items():
    log("User requested list of checklist items", "LOW", "PASS")
    result = checklists_kb.query.group_by(checklists_kb.checklistID).paginate(1, 1500, False)
    return order_checklist_items(result)


def get_checklist_items_lvl(lvl):
    log("User requested list of checklist items based on level", "LOW", "PASS")
    val_num(lvl)
    # ASVS kbID's below 400
    # MASVS kbID's between 400 and 799
    if lvl == 1: # ASVS Level 1
        result = checklists_kb.query.filter((checklists_kb.kbID < 400) & checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1)).group_by(checklists_kb.checklistID).paginate(1, 1500, False)
    elif lvl == 2: # ASVS Level 2
        result = checklists_kb.query.filter((checklists_kb.kbID < 400) & checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1) | checklists_kb.checklist_items.has(level = 2)).group_by(checklists_kb.checklistID).paginate(1, 1500, False)
    elif lvl == 3: # ASVS Level 3
        result = checklists_kb.query.filter((checklists_kb.kbID < 400) & checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1) | checklists_kb.checklist_items.has(level = 2) | checklists_kb.checklist_items.has(level = 3)).group_by(checklists_kb.checklistID).paginate(1, 1500, False)
    elif lvl == 4: # MASVS Level 1
        result = checklists_kb.query.filter((checklists_kb.kbID >= 400) & (checklists_kb.kbID < 1000) & (checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1))).group_by(checklists_kb.checklistID).paginate(1, 1500, False)
    elif lvl == 5: # MASVS Level 2
        result = checklists_kb.query.filter((checklists_kb.kbID >= 400) & (checklists_kb.kbID < 1000) & (checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1) | checklists_kb.checklist_items.has(level = 2))).group_by(checklists_kb.checklistID).paginate(1, 1500, False)
    elif lvl == 6: # MASVS Level R
        result = checklists_kb.query.filter((checklists_kb.kbID >= 400) & (checklists_kb.kbID < 1000) & (checklists_kb.checklist_items.has(level = 0) | checklists_kb.checklist_items.has(level = 1) | checklists_kb.checklist_items.has(level = 2) | checklists_kb.checklist_items.has(level = 'R'))).group_by(checklists_kb.checklistID).paginate(1, 1500, False)
    return order_checklist_items(result, lvl)


def order_checklist_items(checklist_items, lvl):
    ordered_checklist_items = []
    for item in checklist_items.items:
        numbers = item.checklistID.split('.')
        category = int(numbers[0])
        category_requirement = int(numbers[1])
        if (len(ordered_checklist_items) == 0):
            ordered_checklist_items.append(item)
        else:
            y = 0
            while y < len(ordered_checklist_items):
                numbers_ordered = ordered_checklist_items[y].checklistID.split('.')
                category_ordered = int(numbers_ordered[0])
                category_requirement_ordered = int(numbers_ordered[1])
                if (category < category_ordered):
                    ordered_checklist_items.insert(y, item)
                    break
                else:
                    if (category == category_ordered):
                        if (category_requirement < category_requirement_ordered):
                            ordered_checklist_items.insert(y, item)
                            break
                y = y + 1
            if (y == len(ordered_checklist_items)):
                ordered_checklist_items.insert(y, item)

    if (not(lvl == 6)):
        i = 0
        previousItemLevel = -1
        orderedWithEmpties = []
        for item in ordered_checklist_items:
            if ((item.checklist_items.level == 0 and previousItemLevel == 0) or (item.checklist_items.content == "Resiliency Against Reverse Engineering Requirements" and not (lvl == 6))):
                if (item.checklist_items.content == "Resiliency Against Reverse Engineering Requirements"):
                    orderedWithEmpties.append(item)
                    previousItemLevel = item.checklist_items.level
                    checklist_empty = checklists("0.0", "Requirements of Reverse Engineering can be added to form a level " + str(lvl-3) + "+R.", -1, 0)
                    checklists_kb_empty = checklists_kb("0.0", checklist_empty, 0, None)
                    orderedWithEmpties.append(checklists_kb_empty)
                else:
                    checklist_empty = checklists("0.0", "No items for this category in this checklist level", -1, 0)
                    checklists_kb_empty = checklists_kb("0.0", checklist_empty, 0, None)
                    orderedWithEmpties.append(checklists_kb_empty)
                    orderedWithEmpties.append(item)
                    previousItemLevel = item.checklist_items.level
            else:
                orderedWithEmpties.append(item)
                previousItemLevel = item.checklist_items.level
            i = i + 1;
        checklist_items.items = orderedWithEmpties
    else:
        orderedWithR6 = []
        checklist_empty = checklists("0.0", "Using Requirements of Reverse Engineering you can form the levels L1+R or L2+R.", -1, 0)
        checklists_kb_empty = checklists_kb("0.0", checklist_empty, 0, None)
        orderedWithR6.append(checklists_kb_empty)
        for item in ordered_checklist_items:
            if (item.checklist_items.level == 'R'):
                checklist_modified = checklists(item.checklistID, item.checklist_items.content, 6, item.checklist_items.kbID)
                modifiedItem = checklists_kb(item.checklistID, checklist_modified, item.kbID, item.kb_items)
                orderedWithR6.append(modifiedItem)
            else:
                orderedWithR6.append(item)
        checklist_items.items = orderedWithR6
    return checklist_items

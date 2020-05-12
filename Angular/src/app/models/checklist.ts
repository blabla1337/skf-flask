export class Checklist {

  checklist_id?: number;
  include_always?: boolean;
  content?: string;
  question_id?: number;
  cwe?: number;
  checklist_items_checklist_id?: any;
  checklist_items_content?: any;
  checklist_items_level?: any;
  kb_item_title?: any;
  kb_items_content?: any;
  kb_item_id?: any;

  constructor(
    checklist_id?: number,
    include_always?: boolean,
    content?: string,
    question_id?: number,
    cwe?: number,
    checklist_items_checklist_id?: any,
    checklist_items_content?: any,
    checklist_items_level?: any,
    kb_item_title?: any,
    kb_items_content?: any,
    kb_item_id?: any
  ) {

    this.checklist_id = checklist_id;
    this.include_always = include_always;
    this.content = content;
    this.question_id = question_id;
    this.cwe = cwe;
    this.checklist_items_checklist_id = checklist_items_checklist_id;
    this.checklist_items_content = checklist_items_content;
    this.checklist_items_level = checklist_items_level;
    this.kb_item_title = kb_item_title;
    this.kb_items_content = kb_items_content;
    this.kb_item_id = kb_item_id;
  }
}



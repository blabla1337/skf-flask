export type LabLanguage = "python" | "java" | "js" | "net";
// unknown while loading
export type SlideType = "None" | "Unknown" | "Question" | "Answer" | "Slide";
export type ContentItemType = "None" | "Unknown" | "Slides" | "Questionnaire" | "Lab" | "Video" | "Empty";
export type CourseItemType = "Title" | "Topic" | "Category";

export interface Profile {
  id: string;
  name: string;
  text: string;
  iconClass: string;
  courses?: CourseInfo[];
}

export interface LabImage {
  python?: string;
  java?: string;
  js?: string;
  net?: string;
  ruby?: string;
}

export interface Lab {
  hint: string;
  writeup: string;
  images: LabImage[]
}

export interface ContentItem {
  slide?: string;
  video?: string;
  questionnaire?: string;
  lab?: Lab;
}

export interface CourseItem {
  id: string;
  name: string;
  content?: ContentItem[];
  courseItemType?: CourseItemType;
  seen?: boolean;
}

export interface Topic  extends CourseItem {
  categories: Category[];
}

export interface Category extends CourseItem {
}

export interface CourseInfo {
  id: string,
  name: string,
  text: string,
  iconClass: string,
}

export interface Course {
  version: number
  date: string;
  id: string;
  name: string;
  languages: LabLanguage[];
  assetsPath: string;
  content?: ContentItem[];
  topics: Topic[];
}

export interface LanguageInfo {
  code: string;
  name: string;
}

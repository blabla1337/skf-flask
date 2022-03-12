export type LabLanguage = "python" | "java" | "js" | "net";

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
  content: ContentItem[];
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
  content: ContentItem[];
  topics: Topic[];
}

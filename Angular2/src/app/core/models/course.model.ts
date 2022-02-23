export type LabLanguage = "python" | "java" | "js" | "net";

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

export interface Category {
  id: number;
  name: string;
  content: ContentItem[];
}

export interface Topic {
  id: number;
  name: string;
  content: ContentItem[];
  categories: Category[];
}

export interface Course {
  version: number
  date: string;
  id: number;
  name: string;
  languages: LabLanguage[];
  content: ContentItem[];
  topics: Topic[];
}

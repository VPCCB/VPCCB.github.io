import { glob } from 'astro/loaders';
import { defineCollection, z } from 'astro:content';

// Blog posts live in src/content/blog/*.md (or .mdx).
const blog = defineCollection({
  loader: glob({ base: './src/content/blog', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    draft: z.boolean().optional(),
  }),
});

export const collections = { blog };

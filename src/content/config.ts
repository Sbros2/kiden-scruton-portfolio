import { z, defineCollection } from "astro:content";

const projects = defineCollection({
    type: "content",
    schema: z.object({
        title: z.string(),
        discipline: z.string().optional(),
        role: z.string().optional(),
        outcome: z.string().optional(),
        recognition: z.string().optional(),
        order: z.number().optional(),
        date: z.string(),
        summary: z.string().optional(),
        tags: z.array(z.string()).optional(),
        thumbnail: z.string().optional(),
    }),
});

const resources = defineCollection({
    type: "content",
    schema: z.object({
        title: z.string(),
        date: z.string(),
        kind: z.enum(["YouTube", "Game", "Article", "Talk", "Tool", "Other"]).default("Other"),
        href: z.string().url(),
        blurb: z.string().optional(),
        thumbnail: z.string().optional(),
        // Optional fields to render nicer cards
        channel: z.string().optional(),   // for YouTube
        gameType: z.string().optional()   // for Game, e.g., "Factory sim"
    }),
});

export const collections = { projects, resources };

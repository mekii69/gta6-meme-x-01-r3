// gta6-meme-x-01-r3 entrypoint (Node 22, standard library only).
//
// The entry is the X post itself: the house reads the post from X (its
// first picture, the meme, and its text) and hands that to the judge.
// This program only hands the gate the post's address: it copies
// POST.json from the repository root into the output directory, byte
// for byte, and nothing else. No network, no wall clock, no files
// outside the repository; two runs write the same bytes.
//
// The r3 meme is a Leonida Air boarding pass to Vice City, 13 years
// late: the make.fun ghost is the airline's logo in the header, and
// the fields carry the GTA jokes (the wait since Sep 2013, the delays,
// 214 GB, 5 sick days, gate 5 stars, Lucia & Jason as crew). The post
// for r3 must be a NEW X post -- each submission may name a new post,
// and the judge reads the new post's first picture. POST.json starts
// as a placeholder until the user posts; the placeholder is
// deliberately not a real URL, so the entry_link check refuses it
// until the real post exists.
//
// Local run (mirrors the grader's layout):
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const BOT_DIR: string = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const OUTPUT_DIR: string = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const POST_FILE = "POST.json";

function fail(message: string): never {
  console.error(`gta6-meme-x-01-r3: ${message}`);
  process.exit(1);
}

const sourcePath = join(BOT_DIR, POST_FILE);
const targetPath = join(OUTPUT_DIR, POST_FILE);

if (!existsSync(sourcePath)) {
  fail(`no ${POST_FILE} found in ${BOT_DIR}`);
}

let parsed: unknown;
try {
  parsed = JSON.parse(readFileSync(sourcePath, "utf8"));
} catch (err) {
  fail(`${POST_FILE} is not valid JSON: ${(err as Error).message}`);
}

if (
  typeof parsed !== "object" ||
  parsed === null ||
  typeof (parsed as { url?: unknown }).url !== "string"
) {
  fail(`${POST_FILE} must be a JSON object with a string "url"`);
}

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(sourcePath, targetPath);
} catch (err) {
  fail(`could not copy ${POST_FILE} to ${OUTPUT_DIR}: ${(err as Error).message}`);
}

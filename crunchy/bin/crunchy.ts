#!/usr/bin/env bun
import { $ } from "bun";
import { existsSync, writeFileSync } from "fs";
import path from "path";

const ROOT = path.resolve(import.meta.dir, "../../");
const SKILLS = path.join(ROOT, ".pi/skills");

async function runSkill(skill: string, script: string, args: string[] = []) {
  const scriptPath = path.join(SKILLS, skill, "scripts", script);
  if (!existsSync(scriptPath)) {
    return `Error: ${scriptPath} not found.`;
  }
  try {
    const result = await $`cd ${ROOT} && bash ${scriptPath} ${args}`.text();
    return result.trim() || "(no output)";
  } catch (err) {
    return `Failed to run ${skill}/${script}: ${err}`;
  }
}

async function main() {
  console.log("🦃 Crunchy-CI: Starting repository health check...");

  const report: string[] = [];
  report.push("# 🍎 Crunchy-CI Health Report");
  report.push(`Generated on: ${new Date().toISOString()}\n`);

  // 1. Structure
  console.log("  - Mapping repository structure...");
  const tree = await runSkill("repo-analyzer", "map_tree.sh");
  report.push("## 🌳 Project Structure");
  report.push("```");
  report.push(tree);
  report.push("```\n");

  // 2. Technical Debt
  console.log("  - Hunting for TODOs...");
  const todos = await runSkill("code-critic", "find_todos.sh");
  report.push("## 📝 Technical Debt (TODOs/FIXMEs)");
  report.push("```");
  report.push(todos);
  report.push("```\n");

  // 3. Performance
  console.log("  - Auditing file sizes...");
  const sizes = await runSkill("performance-auditor", "check_file_sizes.sh");
  report.push("## ⚖️ Large Files (>100KB)");
  report.push("```");
  report.push(sizes);
  report.push("```\n");

  // 4. Test Coverage
  console.log("  - Checking for missing tests...");
  const missingTests = await runSkill("test-gen", "find_missing_tests.sh", ["lifecycle"]);
  report.push("## 🧪 Test Coverage Gaps");
  report.push("```");
  report.push(missingTests);
  report.push("```\n");

  const reportPath = path.join(ROOT, "REPORT.md");
  writeFileSync(reportPath, report.join("\n"));
  
  console.log(`\n✅ Health check complete! Report saved to: ${reportPath}`);
}

main().catch(console.error);

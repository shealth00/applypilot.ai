import type { NextConfig } from "next";

const basePath = process.env.NEXT_PUBLIC_BASE_PATH ?? "";
const outputMode = process.env.NEXT_OUTPUT_MODE ?? "standalone";

const nextConfig: NextConfig =
  outputMode === "export"
    ? {
        output: "export",
        ...(basePath ? { basePath, assetPrefix: basePath } : {}),
        images: {
          unoptimized: true,
        },
      }
    : {
        output: "standalone",
      };

export default nextConfig;

import React from "react";
import FileUpload from "./_components/FileUpload";
import { FilePreview } from "./_components/FilePreview";

const page = () => {
  return (
    <div className="min-h-screen border-l-2 ml-2 p-6 flex-col justify-center">
      <h1 className="text-3xl font-bold mb-6 text-center text-dark-1">
        Start <strong className="text-light-2">Uploading</strong> your Files and{" "}
        <strong className="text-light-2">Grade</strong> it
      </h1>

      <div className="space-y-4">
        <FileUpload />
      </div>
    </div>
  );
};

export default page;

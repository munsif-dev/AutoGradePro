"use client";
import { Files } from "lucide-react";
import React from "react";
import { FilePreview } from "./FilePreview";

const FileUpload = () => {
  const [file, setFile] = React.useState(null);
  const onFileSelect = (file) => {
    if (file && file.size > 6000000) {
      alert("File size is too large");
      return;
    }
    setFile(file);
  };
  return (
    <div className="text-center">
      <div className="flex-col justify-center  space-y-2 w-full bg-transparent ">
        <label
          htmlFor="dropzone-file"
          className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-purple-50  hover:bg-purple-200 "
        >
          <div className="flex flex-col items-center justify-center pt-5 pb-6">
            <svg
              className="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 20 16"
            >
              <path
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"
              />
            </svg>
            <p className="mb-2 text-sm text-gray-500 dark:text-gray-400">
              <span className="font-semibold">Click to upload</span> or{" "}
              <span className="text-light-2">drag</span> and{" "}
              <span className="text-light-2">drop</span>
            </p>
            <p className="text-xs text-gray-500 dark:text-gray-400">
              SVG, PNG, JPG or GIF (MAX 6MB)
            </p>
          </div>
          <input
            id="dropzone-file"
            type="file"
            className="hidden"
            onChange={(event) => {
              onFileSelect(event.target.files[0]);
            }}
          />
        </label>
        <div className="w-full flex  space-x-2 justify-center items-center">
          <button
            disabled={!file}
            className="px-4 py-2 mt-4 text-sm text-center font-medium 
           bg-light-2  hover:bg-light-1  text-white 
           rounded-full  disabled:bg-gray-600 "
          >
            Upload
          </button>
          <div className="w-full">
            <FilePreview file={file} removeFile={() => setFile(null)} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default FileUpload;

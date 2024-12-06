let pkgs = import <nixpkgs> { config.allowUnfree = true; };

in pkgs.mkShell rec {
  name = "python-dev";

  buildInputs = with pkgs; [
    python312
    python312Packages.requests
    python312Packages.langdetect
    python312Packages.mecab-python3
    python312Packages.unidic-lite
    python312Packages.mwparserfromhell
    python312Packages.tqdm
    python312Packages.fugashi
    python312Packages.unidic-lite
    python312Packages.torchWithCuda
    python312Packages.torchvision
    python312Packages.torchaudio
    python312Packages.transformers
    python312Packages.sentence-transformers
  ];
  shellHook = ''
      export CUDA_PATH=${pkgs.cudatoolkit}
      export LD_LIBRARY_PATH=/usr/lib/wsl/lib:${pkgs.linuxPackages.nvidia_x11}/lib:${pkgs.ncurses5}/lib
      export EXTRA_LDFLAGS="-L/lib -L${pkgs.linuxPackages.nvidia_x11}/lib"
      export EXTRA_CCFLAGS="-I/usr/include"
  '';
}

// Types for Qt WebChannel integration
declare global {
  interface Window {
    qt?: {
      webChannelTransport: any;
    };
    backend?: {
      getDocuments(): any;
      createObject(params: any): any;
      objectCreated: {
        connect(callback: (info: any) => void): void;
      };
      selectionChanged: {
        connect(callback: (payload: any) => void): void;
      };
    };
  }
}

export {};
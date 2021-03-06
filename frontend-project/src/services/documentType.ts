import smallEodSDK from '@/utils/sdk';

import { DocumentType } from './definitions';

export const fetchDocumentType = async (id: number): Promise<DocumentType> => {
  const response = await new smallEodSDK.DocumentTypesApi().documentTypesRead(id);
  return response;
};
